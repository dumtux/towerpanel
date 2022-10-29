<script lang="ts">
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';
	import { Divider, FileDropzone, DataTable } from '@brainandbones/skeleton';
    import { humanFileSize } from '$lib/utilities/misc/filesize';
    export let releases_url: string = 'https://api.github.com/repos/[USER]/[REPO]/releases';
	export let upgrading_target: string = "[TARGET]";

    const max_file_size = "20MB";
    let files: FileList;
    let filename = '';
    let filesize = '';
    let is_big = false;

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
                throw new Error("There is not an official release yet.");
            }
            const releases = res.map((element) => {
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
            throw new Error("Cannot get repository data: " + http.status);
        }
    }
    let tablePromise: Promise<any> = getTableSource();
</script>

<section class="space-y-4">
    <section class="card card-body space-y-4">
        <h3>Online Resources</h3>
        {#await tablePromise}
            <p class="text-center">Loading...</p>
        {:then response}
            <DataTable
                headings={tableServer.headings}
                source={response}
            >
            </DataTable>
        {:catch error}
            <p style="text-center text-warning-500">{error.message}</p>
        {/await}
    </section>
    <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible={is_big}>
        <span>
            File size cannot be bigger than {max_file_size}.
        </span>
    </Alert>
    <section class="card card-body space-y-4">
        <h3>Local File</h3>
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
