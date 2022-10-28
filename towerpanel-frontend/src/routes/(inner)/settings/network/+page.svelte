<script lang="ts">
	import { writable, type Writable } from "svelte/store";
	import { Divider, TabGroup, Tab } from '@brainandbones/skeleton';
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';

	const storeTab: Writable<string> = writable('routing');
</script>

<div class="page-container">
	<TabGroup selected={storeTab}>
		<Tab value="routing">Routing</Tab>
		<Tab value="ethernet">Ethernet</Tab>
		<Tab value="wifi">Wi-Fi</Tab>
		<Tab value="cellular">Cellular</Tab>
	</TabGroup>

	<!-- Conditionally display content -->
	{#if $storeTab === 'routing'}
		<section class="space-y-4">
			<!-- <h1>GNSS</h1> -->
			<Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible=true>
				<span>
					This page is not implemented yet
				</span>
			</Alert>
		</section>
	{/if}

	{#if $storeTab === 'ethernet'}
        <section class="space-y-4">
            <!-- <h1>GNSS</h1> -->
            <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible=true>
                <span>
                    This page is not implemented yet
                </span>
            </Alert>
        </section>
    {/if}

	{#if $storeTab === 'wifi'}
        <section class="space-y-4">
            <!-- <h1>GNSS</h1> -->
            <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible=true>
                <span>
                    This page is not implemented yet
                </span>
            </Alert>
        </section>
    {/if}

	{#if $storeTab === 'cellular'}
        <section class="space-y-4">
            <!-- <h1>GNSS</h1> -->
            <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible=true>
                <span>
                    This page is not implemented yet
                </span>
            </Alert>
        </section>
    {/if}

</div>
