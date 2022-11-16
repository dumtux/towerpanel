<script lang="ts">
	// Components
	import Avatar from '@brainandbones/skeleton/components/Avatar/Avatar.svelte';
	import SvgIcon from '$lib/components/SvgIcon/SvgIcon.svelte';
    import * as THREE from 'three';
    import NET from 'vanta/dist/vanta.net.min';
	import { storeLightSwitch } from '@brainandbones/skeleton/utilities/LightSwitch/stores';
	import { onMount } from 'svelte';
    import Auth from '$lib/components/Auth/Auth.svelte';

	let bg: NET = null;

	$: $storeLightSwitch, onLightModeChange();

	function onLightModeChange() {
		if (bg) {
			bg.destroy();
		}
		if ($storeLightSwitch) {
			bg = initBackground(0x010f18);
		} else {
			bg = initBackground(0xf8f8f8);
		}
	}

	function initBackground(color: number) {
		bg = NET({
            el: "#homepage",
            THREE: THREE,
			mouseControls: true,
			touchControls: true,
			gyroControls: false,
			minHeight: 200.00,
			minWidth: 200.00,
			scale: 1.00,
			scaleMobile: 1.00,
			color: 0x7accfe,
			backgroundColor: color
		});
	}

	onMount(async () => {
		onLightModeChange();
	});

	let visible: boolean = true;
	function toggleVisible(): void {
		visible = !visible;
	}
</script>

<!-- <div use:vanta> -->
<div id="homepage" class="h-[calc(100vh-5.5rem)] items-center">
		<Auth />
</div>
