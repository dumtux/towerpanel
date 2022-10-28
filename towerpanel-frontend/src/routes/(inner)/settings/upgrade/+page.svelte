<script lang="ts">
	import { writable, type Writable } from "svelte/store";
	import { Divider, TabGroup, Tab, FileDropzone } from '@brainandbones/skeleton';
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';
    import { humanFileSize } from '$lib/utilities/misc/filesize';

	const storeTab: Writable<string> = writable('local');
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
</script>

<div class="page-container">
	<TabGroup selected={storeTab}>
		<Tab value="local">Manual Update</Tab>
		<Tab value="tower">Online Repo</Tab>
	</TabGroup>

	<!-- Conditionally display content -->
	{#if $storeTab === 'tower'}
		<section class="space-y-4">
			<!-- <h1>GNSS</h1> -->
			<Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible=true>
				<span>
					This page is not implemented yet
				</span>
			</Alert>
		</section>
	{/if}

	{#if $storeTab === 'local'}
        <section class="space-y-4">
            <!-- <h1>GNSS</h1> -->
            <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible={is_big}>
                <span>
                    File size cannot be bigger than 20.0MB.
                </span>
            </Alert>
            <section class="card card-body space-y-4">
                <FileDropzone bind:files on:change={onChange} notes="Files should not exceed 5mb." />

                {#if files }
                   <Divider />
                   <p>{filename}</p>
                   <p>{filesize}</p>
                   <Divider />
                   <button class="btn bg-primary-500 btn-base text-white" on:click={onUpload} disabled={is_big}>Upload & Upgrade</button>
                   {/if}
            </section>
        </section>
    {/if}

</div>
