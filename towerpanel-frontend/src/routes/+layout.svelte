<!-- Layout: (root) -->
<script lang="ts">
	import hljs from 'highlight.js';
	import '@brainandbones/skeleton/styles/highlight-js.css'; // was: 'highlight.js/styles/github-dark.css';
	import { storeHighlightJs } from '@brainandbones/skeleton/utilities/CodeBlock/stores';
	storeHighlightJs.set(hljs);

	// SvelteKit Imports
	import { browser } from '$app/environment';
	import { page } from '$app/stores';
	import { afterNavigate } from '$app/navigation';

	// Stores
	import { storeCurrentUrl, storeTheme } from '$panel/stores';
	import { storePreview } from '$panel/PanelThemer/stores';

	// Components & Utilities
	import AppShell from '@brainandbones/skeleton/components/AppShell/AppShell.svelte';
	import Dialog from '@brainandbones/skeleton/utilities/Dialog/Dialog.svelte';
	import Toast from '@brainandbones/skeleton/utilities/Toast/Toast.svelte';

	// Docs Components
	import DocsAppBar from '$panel/PanelAppBar/PanelAppBar.svelte';
	import DocsSidebar from '$panel/PanelNavigation/PanelSidebar.svelte';
	import DocsDrawer from '$panel/PanelNavigation/PanelDrawer.svelte';
	import DocsFooter from '$panel/PanelFooter/PanelFooter.svelte';

	// Themes
	// https://vitejs.dev/guide/features.html#disabling-css-injection-into-the-page
	import rocket from '@brainandbones/skeleton/themes/theme-rocket.css?inline';
	import modern from '@brainandbones/skeleton/themes/theme-modern.css?inline';
	import seafoam from '@brainandbones/skeleton/themes/theme-seafoam.css?inline';
	import vintage from '@brainandbones/skeleton/themes/theme-vintage.css?inline';
	import sahara from '@brainandbones/skeleton/themes/theme-sahara.css?inline';
	// import seasonal from '$lib/themes/theme-seasonal.css?inline';

	// Default Theme, injected immediately:
	import skeleton from '@brainandbones/skeleton/themes/theme-skeleton.css';
	// Skeleton Stylesheets
	import '@brainandbones/skeleton/styles/all.css';
	// Global Stylesheets
	import '../app.postcss';

	// List of Themes
	const themes: any = { skeleton, rocket, modern, seafoam, vintage, sahara };

	// Set body `data-theme` based on current theme status
	storeTheme.subscribe(setBodyThemeAttribute);
	storePreview.subscribe(setBodyThemeAttribute);
	function setBodyThemeAttribute(): void {
		if (!browser) return;
		document.body.setAttribute('data-theme', $storePreview ? 'generator' : $storeTheme);
	}

	// Lifecycle Events
	afterNavigate((params: any) => {
		// Store current page route URL
		storeCurrentUrl.set($page.url.pathname);
		// Scroll to top
		const isNewPage: boolean = params.from && params.to && params.from.routeId !== params.to.routeId;
		const elemPage = document.querySelector('#page');
		if (isNewPage && elemPage !== null) {
			elemPage.scrollTop = 0;
		}
	});

	// Disable left sidebar on homepage
	$: slotSidebarLeft = $page.url.pathname === '/' ? 'w-0' : 'bg-white/20 dark:bg-black/5 lg:w-auto';
</script>

<svelte:head>
	<!-- Select Preset Theme CSS -->
	{@html `\<style\>${themes[$storeTheme]}}\</style\>`}
</svelte:head>

<!-- Overlays -->
<Dialog />
<Toast />
<DocsDrawer />

<!-- App Shell -->
<AppShell {slotSidebarLeft} slotFooter="bg-black p-4">
	<!-- Header -->
	<svelte:fragment slot="header">
		<DocsAppBar />
	</svelte:fragment>

	<!-- Sidebar (Left) -->
	<svelte:fragment slot="sidebarLeft">
		<DocsSidebar class="hidden lg:block w-[280px]" />
	</svelte:fragment>

	<!-- Page Content -->
	<slot />

	<!-- Page Footer -->
	<!-- <svelte:fragment slot="pageFooter">
		<DocsFooter />
	</svelte:fragment> -->
</AppShell>
