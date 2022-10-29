<script lang="ts">
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';
	import { Divider, FileDropzone, DataTable } from '@brainandbones/skeleton';
    import { humanFileSize } from '$lib/utilities/misc/filesize';

    export let releases_url: string = 'https://api.github.com/repos/[USER]/[REPO]/releases';
    export let upgrading_target: string = "[TARGET]";

    const max_file_size = "20MB";
    let files: FileList;
    let filename: string = '';
    let filesize: string | number = '';
    let is_big: boolean = false;
    let fetch_error_text: string = '';
    let is_fetch_error: boolean = false;

	function onChange(e: any): void {
        filename = files[0].name;
        filesize = humanFileSize(files[0].size);
        is_big = files[0].size > 20971520;
	}

	function onUpload(e: any): void {
        console.log("Uploading ...");
	}

    const tableServer: any = { search: undefined, sort: undefined, headings: undefined, count: 0 };

    async function getTableSource(): Promise<any> {
        const http = await fetch(releases_url);
        if (http.ok) {
            const res = await http.json();
            if (res.length == 0) {
                fetch_error_text = "There is not an official release yet.";
                is_fetch_error = true;
                return;
            }
            const releases = res.map((element) => {
                fetch_error_text = "";
                is_fetch_error = false;
                return {
                    id: element["id"],
                    name: element["name"],
                    tag_name: element["tag_name"],
                    prerelease: element["prerelease"],
                    published_at: element["published_at"],
                };
            });
            tableServer.headings = Object.keys(releases[0]);
            return releases;
        } else {
            fetch_error_text = "Cannot fetch from remote repository, check internet connection: " + http.status;
            is_fetch_error = true;
        }
    }
    let tablePromise: Promise<any> = getTableSource();

    function onSelect(e) {
        console.log(e.detail);
    }
</script>

<section class="space-y-4">
    <section class="card card-body space-y-4">
        <h3>Online Resources</h3>
        <p>Select a version from the official repository to upgrade.</p>
        <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible={is_fetch_error}>
            <span>
                Cannot get repository data: {fetch_error_text}.
            </span>
        </Alert>
        {#await tablePromise}
            <p class="text-center">Loading...</p>
        {:then response}
            <DataTable
                headings={tableServer.headings}
                source={response}
                interactive
                on:selected={onSelect}
            >
            </DataTable>
        {:catch error}
            <p style="text-center text-warning-500">{error.message}</p>
        {/await}
    </section>
    <section class="card card-body space-y-4">
        <h3>Local File</h3>
        <p>Upload from a local binary or zip file to upgrade.</p>
        <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible={is_big}>
            <span>
                File size cannot be bigger than {max_file_size}.
            </span>
        </Alert>
        <FileDropzone bind:files on:change={onChange} notes="Files should not exceed {max_file_size}" />

        {#if files }
            <Divider />
            <p>{filename}</p>
            <p>{filesize}</p>
            <Divider />
            <button class="btn bg-primary-500 btn-base text-white" on:click={onUpload} disabled={is_big}>Upload & Upgrade</button>
            {/if}
    </section>
</section>
