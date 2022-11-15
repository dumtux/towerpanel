<script lang="ts">
	// Components
	import Avatar from '@brainandbones/skeleton/components/Avatar/Avatar.svelte';
	import SvgIcon from '$lib/components/SvgIcon/SvgIcon.svelte';
    import * as THREE from 'three';
    import NET from 'vanta/dist/vanta.net.min';
	import { storeLightSwitch } from '@brainandbones/skeleton/utilities/LightSwitch/stores';
	import { onMount } from 'svelte';

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
<div id="homepage" class="h-[calc(100vh-5.5rem)]">

	<div class="container max-w-[1200px] mx-auto px-4 py-10 md:py-20 space-y-20">

		<!-- Team -->
		<section class="text-center space-y-6">
			<h2>Meet The Team</h2>
			<ul class="grid grid-cols-1 md:grid-cols-2 gap-4">
				<li class="card card-body space-y-2 text-center">
					<Avatar src="/image/avata-jtsheedy.jpeg" width="w-24" shadow="shadow-xl" class="mx-auto" />
					<h4>jtsheedy</h4>
					<p>Managing Director @ TowerSoftware Ltd</p>
					<div class="flex justify-center space-x-4">
						<a href="https://github.com/jtsheedy" target="_blank" rel="noreferrer"><SvgIcon name="github" /></a>
						<a href="https://mobile.twitter.com/jtsheedy" target="_blank" rel="noreferrer"><SvgIcon name="twitter" /></a>
						<a href="https://www.linkedin.com/in/jtsheedy" target="_blank" rel="noreferrer"><SvgIcon name="linkedin" /></a>
					</div>
				</li>
				<li class="card card-body space-y-2 text-center">
					<Avatar src="/image/avata-dumtux.jpeg" width="w-24" shadow="shadow-xl" class="mx-auto" />
					<h4>dumtux</h4>
					<p>Linux Developer and Hardware Designer</p>
					<div class="flex justify-center space-x-4">
						<a href="https://github.com/dumtux" target="_blank" rel="noreferrer"><SvgIcon name="github" /></a>
					</div>
				</li>
			</ul>
		</section>

	</div>
</div>
