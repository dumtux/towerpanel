<script lang="ts">
	import Drawer from '@brainandbones/skeleton/utilities/Drawer/Drawer.svelte';
	import PanelSidebar from './PanelSidebar.svelte';
	import { storeMobileDrawer } from '$panel/stores';
</script>

<Drawer open={storeMobileDrawer} display="lg:hidden">
	<PanelSidebar embedded={true} />
</Drawer>
