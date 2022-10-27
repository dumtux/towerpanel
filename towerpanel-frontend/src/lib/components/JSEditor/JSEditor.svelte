<script lang="ts">
    import type monaco from 'monaco-editor';
    import { onMount } from 'svelte';
    import editorWorker from 'monaco-editor/esm/vs/editor/editor.worker?worker';
    import jsonWorker from 'monaco-editor/esm/vs/language/json/json.worker?worker';
    import cssWorker from 'monaco-editor/esm/vs/language/css/css.worker?worker';
    import htmlWorker from 'monaco-editor/esm/vs/language/html/html.worker?worker';
    import tsWorker from 'monaco-editor/esm/vs/language/typescript/ts.worker?worker';
	import { Divider, DataTable } from '@brainandbones/skeleton';
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';

    let divEl: HTMLDivElement = null;
    let editor: monaco.editor.IStandaloneCodeEditor;
    let Monaco;

    const DEFAULT_PARSER = `function parse(data) {
	return {
        headings: ['Parameter', 'Value', 'Unit / Type'],
        body: [
            { parameter: 'Raw Data', value: data, unit: 'str' },
            { parameter: 'X', value: 1.0, unit: '?' },
            { parameter: 'Y', value: 1.0, unit: '?' },
        ]
    };
}`;

    onMount(async () => {
        // @ts-ignore
        self.MonacoEnvironment = {
            getWorker: function (_moduleId: any, label: string) {
                if (label === 'json') {
                    return new jsonWorker();
                }
                if (label === 'css' || label === 'scss' || label === 'less') {
                    return new cssWorker();
                }
                if (label === 'html' || label === 'handlebars' || label === 'razor') {
                    return new htmlWorker();
                }
                if (label === 'typescript' || label === 'javascript') {
                    return new tsWorker();
                }
                return new editorWorker();
            }
        };

        Monaco = await import('monaco-editor');
        editor = Monaco.editor.create(divEl, {
            value: DEFAULT_PARSER,
            language: 'javascript',
            theme: 'vs-dark',
            automaticLayout: true
        });

        return () => {
            editor.dispose();
        };
    });

    let headings: string[] = [];
    let source: any[] = [];
    let parser = (data) => [];
    let alert_syntax_visible = false;
    let syntax_error = '';

    function update(data) {
        let result = parser(data);
        headings = result.headings;
        source = result.body;
    }

    function onApply() {
        function looseJsonParse(obj) {
            return Function(`"use strict";return (${obj})`)();
        }
        try {
            parser = looseJsonParse(editor.getValue())
            alert_syntax_visible = false;
            update("data")
        }
        catch (e) {
            alert_syntax_visible = true;
            syntax_error = e;
        }
    }
</script>

<section class="space-y-4">
    <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible={alert_syntax_visible}>
        <h2>JS Parsing Error</h2>
        <span>{syntax_error}</span>
    </Alert>
    <section class="grid grid-cols-2 gap-4">
        <div class="col-span-1 card card-body space-y-4">
            <DataTable {headings} {source}></DataTable>
        </div>
        <div class="col-span-1 card card-body space-y-4">
            <div bind:this={divEl} class="h-96" />
            <button class="btn bg-primary-500 btn-base text-white" on:click={onApply}>Apply</button>
        </div>
    </section>
</section>
