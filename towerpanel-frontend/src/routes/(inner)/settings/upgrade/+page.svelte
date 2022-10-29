<script lang="ts">
	import { writable, type Writable } from "svelte/store";
	import { TabGroup, Tab } from '@brainandbones/skeleton';
    import Upgrader from '$lib/components/Upgrader/Upgrader.svelte';

	const storeTab: Writable<string> = writable('towerwrt');
</script>

<div class="page-container">
	<TabGroup selected={storeTab}>
		<Tab value="towerwrt">TowerWrt</Tab>
		<Tab value="towerpanel">TowerPanel</Tab>
	</TabGroup>

	<!-- Conditionally display content -->
	{#if $storeTab === 'towerwrt'}
        <Upgrader
			releases_url="https://api.github.com/repos/dumtux/towerwrt/releases"
			upgrading_target="towerwrt"
		/>
    {/if}
    {#if $storeTab === 'towerpanel'}
    <Upgrader
		releases_url="https://api.github.com/repos/dumtux/towerpanel/releases"
		upgrading_target="towerpanel"
		/>
    {/if}

</div>
