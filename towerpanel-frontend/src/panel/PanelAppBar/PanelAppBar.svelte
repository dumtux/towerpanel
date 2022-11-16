<script lang="ts">
	// @ts-ignore
	const pkg = __PACKAGE__;

	// Components
	import AppBar from '@brainandbones/skeleton/components/AppBar/AppBar.svelte';
	import Divider from '@brainandbones/skeleton/components/Divider/Divider.svelte';
	import SvgIcon from '@brainandbones/skeleton/components/SvgIcon/SvgIcon.svelte';
	// Utilities
	import LightSwitch from '@brainandbones/skeleton/utilities/LightSwitch/LightSwitch.svelte';
	import { menu } from '@brainandbones/skeleton/utilities/Menu/menu';

	// Stores
	import { storeTheme, storeMobileDrawer } from '$panel/stores';

	// Drawer Handler
	function drawerOpen(): void {
		storeMobileDrawer.set(true);
	}

	// Sidebar Scroll Handler
	function scrollSidebarTo(targetId: string): void {
		const elemSidebarLeft: HTMLElement | null = document.querySelector('#sidebar-left');
		const targetElem: HTMLElement | null = document.querySelector(targetId);
		const targetOffsetTop = targetElem?.offsetTop;
		if (elemSidebarLeft && targetOffsetTop) {
			elemSidebarLeft.scrollTo({ top: targetOffsetTop - 160, behavior: 'smooth' });
		}
	}
</script>

<AppBar border="border-b border-b-surface-300 dark:border-b-surface-900">
	<!-- Branding -->
	<svelte:fragment slot="lead">
		<!-- Drawer Menu -->
		<button on:click={drawerOpen} class="lg:hidden mr-2 p-1 cursor-pointer">
			<SvgIcon name="bars" width="w-6" height="h-6" fill="fill-black dark:fill-white" />
		</button>
		<!-- Skeleton -->
		<a href="/" class="hidden sm:inline-block text-sm sm:text-lg md:text-3xl font-bold uppercase mr-4" title="Return to Homepage">TowerPanel</a>
		<!-- Badge -->
		<a class="hidden sm:block" href="https://github.com/Brain-Bones/skeleton/releases" target="_blank" rel="noreferrer">
			<span class="badge badge-filled-surface">v{pkg.version}</span>
		</a>
	</svelte:fragment>

	<!-- Navigation -->
	<svelte:fragment slot="trail">
		<!-- Theme -->
		<!-- prettier-ignore -->
		<div class="relative">
			<button class="btn btn-sm" use:menu={{ menu: 'theme' }}>
				<SvgIcon name="swatchbook" width="w-4" height="w-4" />
				<span class="hidden md:inline-block">Theme</span>
				<span class="opacity-50">▾</span>
			</button>
			<div class="card card-body w-56 shadow-xl space-y-6" data-menu="theme">
				<section class="flex justify-between">
					<h6>Set Mode</h6>
					<LightSwitch origin="tr" />
				</section>
				<hr>
				<nav class="list-nav">
					<ul>
						<li class="option" class:!bg-primary-500={$storeTheme === 'skeleton'} on:click={() => { storeTheme.set('skeleton') }} on:keypress> 
							<span>💀</span>
							<span>Skeleton</span>
						</li>
						<li class="option" class:!bg-primary-500={$storeTheme === 'modern'} on:click={() => { storeTheme.set('modern') }} on:keypress>
							<span>🤖</span>
							<span>Modern</span>
						</li>
						<li class="option" class:!bg-primary-500={$storeTheme === 'rocket'} on:click={() => { storeTheme.set('rocket') }} on:keypress> 
							<span>🚀</span>
							<span>Rocket</span>
						</li>
						<li class="option" class:!bg-primary-500={$storeTheme === 'seafoam'} on:click={() => { storeTheme.set('seafoam') }} on:keypress>
							<span>🐚</span>
							<span>Seafoam</span>
						</li>
						<li class="option" class:!bg-primary-500={$storeTheme === 'vintage'} on:click={() => { storeTheme.set('vintage') }} on:keypress>
							<span>📺</span>
							<span>Vintage</span>
						</li>
						<li class="option" class:!bg-primary-500={$storeTheme === 'sahara'} on:click={() => { storeTheme.set('sahara') }} on:keypress>
							<span>🏜️</span>
							<span>Sahara</span>
						</li>
						<!-- <li class="option" class:!bg-primary-500={$storeTheme === 'hamlindigo'} on:click={() => { storeTheme.set('hamlindigo') }} on:keypress>
							<span>👔</span>
							<span>Hamlindigo</span>
						</li>
						<li class="option" class:!bg-primary-500={$storeTheme === 'goldNouveau'} on:click={() => { storeTheme.set('goldNouveau') }} on:keypress>
							<span>💫</span>
							<span>Gold Nouveau</span>
						</li>
						<li class="option" class:!bg-primary-500={$storeTheme === 'crimson'} on:click={() => { storeTheme.set('crimson') }} on:keypress>
							<span>⭕</span>
							<span>Crimson</span>
						</li>
						<li class="option" class:!bg-primary-500={$storeTheme === 'test'} on:click={() => { storeTheme.set('test') }} on:keypress>
							<span>🚧</span>
							<span>Test</span>
						</li>
						<li class="option" class:!bg-primary-500={$storeTheme === 'seasonal'} on:click={() => { storeTheme.set('seasonal') }} on:keypress>
							<span>🎃</span>
							<span>Seasonal</span>
						</li> -->
					</ul>
				</nav>
			</div>
		</div>

		<Divider vertical borderWidth="border-l-2" />

		<!-- Community -->
		<section class="flex">
			<a class="btn btn-sm" href="https://linkedin.com/company/towersoftwareltd" target="_blank" rel="noreferrer" aria-label="Discord">
				<SvgIcon name="linkedin" viewBox="0 0 640 512" />
			</a>
			<a class="btn btn-sm" href="https://twitter.com/tower_software" target="_blank" rel="noreferrer" aria-label="Twitter">
				<SvgIcon name="twitter" />
			</a>
			<a class="btn btn-sm" href="https://github.com/dumtux/omega2-4g-gateway" target="_blank" rel="noreferrer" aria-label="GitHub">
				<SvgIcon name="github" />
			</a>
		</section>
	</svelte:fragment>
</AppBar>
