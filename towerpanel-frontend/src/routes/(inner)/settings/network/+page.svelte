<script lang="ts">
	import { writable, type Writable } from "svelte/store";
	import { Divider, TabGroup, Tab, RadioGroup, RadioItem, ListBox, ListBoxItem } from '@brainandbones/skeleton';
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';

    import { diagRouting, diagRoutingWifiAP } from '$lib/components/NetworkConfig/diag.js';

	const storeTab: Writable<string> = writable('ethernet');

    const uplinkMode: Writable<string> = writable("ethernet");
    const downLinkMode: Writable<string[]> = writable(["sw0", "sw1", "sw2", "sw3"]);

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
            <section class="grid grid-cols-1 lg:grid-cols-2 gap-4 card">
                <!-- Single -->
                <div class="card card-body space-y-4">
                    <ListBox selected={uplinkMode} label="Up-Link" hover="bg-accent-hover-token" accent="!bg-accent-active-token">
                        <ListBoxItem value={'ethernet'}>Ethernet</ListBoxItem>
                        <ListBoxItem value={'wifi'}>Wi-Fi</ListBoxItem>
                        <ListBoxItem value={'cellular'}>Cellular</ListBoxItem>
                    </ListBox>
                    <p class="text-center">Selected: <code>{$uplinkMode}</code></p>
                </div>
                <!-- Multiple -->
                <div class="card card-body space-y-4">
                    <ListBox selected={downLinkMode} label="Down-Link">
                        <ListBoxItem value={'sw0'}>Port 0 (ext 0)</ListBoxItem>
                        <ListBoxItem value={'sw1'}>Port 1 (ext 1)</ListBoxItem>
                        <!-- <ListBoxItem value={'sw2'}>Port 2</ListBoxItem> -->
                        <ListBoxItem value={'sw3'}>Port 3 (Vega-28)</ListBoxItem>
                        <!-- <ListBoxItem value={'sw4'}>Port 4</ListBoxItem> -->
                    </ListBox>
                    <p class="text-center">Selected: <code>{$downLinkMode}</code></p>
                </div>
            </section>
            <section class="card">
                <pre class="asciiart"><code>{diagRouting}</code></pre>
            </section>
        </section>
	{/if}

	{#if $storeTab === 'ethernet'}
        <section class="space-y-4">
            <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible=true>
                <span>
                    This page is not implemented yet
                </span>
            </Alert>
        </section>
    {/if}

	{#if $storeTab === 'wifi'}
        <section class="space-y-4">
            <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible=true>
                <span>
                    This page is not implemented yet
                </span>
            </Alert>
        </section>
    {/if}

	{#if $storeTab === 'cellular'}
        <section class="space-y-4">
            <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible=true>
                <span>
                    This page is not implemented yet
                </span>
            </Alert>
        </section>
    {/if}

</div>

<style>
    pre.asciiart, pre.asciiart > code {
        line-height: 1em;
        font-size: 1em;
        font-family: monospace;
        background-color: transparent;
        white-space: none;
        text-align: left;
    }
</style>