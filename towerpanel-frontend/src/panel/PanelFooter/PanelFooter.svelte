<script lang="ts">
	import Divider from '@brainandbones/skeleton/components/Divider/Divider.svelte';
	import SvgIcon from '@brainandbones/skeleton/components/SvgIcon/SvgIcon.svelte';

	// Base Classes
	const cBase: string = 'bg-white/20 dark:bg-black/10 text-xs md:text-base mx-auto px-4 py-8 md:p-10 space-y-10';
	const cRowOne: string = 'flex flex-col md:flex-row justify-between items-center md:items-start space-y-5 md:space-y-0';
	const cRowTwo: string = 'flex flex-col md:flex-row justify-between items-center md:items-start space-y-4 md:space-y-0';
</script>

<div class="page-footer {cBase}">
	<!-- Row 1 -->
	<section class={cRowOne}>
		<div class="space-y-2">
			<span class="text-2xl font-bold uppercase">TowerPanel</span>
			<p class="text-lg opacity-80">Operating Panel Webapp for TowerController III.</p>
		</div>
		<div class="hidden md:flex items-start space-x-10">
			<div class="space-y-4">
				<h6>About</h6>
				<ul class="space-y-2">
					<li><a href="http://www.towersoftwareltd.com/">Company</a></li>
					<li><a href="http://www.towersoftwareltd.com/">Why TowerPanel</a></li>
				</ul>
			</div>
			<div class="space-y-4">
				<h6>Project</h6>
				<ul class="space-y-2">
					<li><a href="https://github.com/dumtux/omega2-4g-gateway" target="_blank" rel="noreferrer">TowerController III</a></li>
					<li><a href="https://github.com/dumtux/towerwrt" target="_blank" rel="noreferrer">TowerWrt</a></li>
					<li><a href="https://github.com/dumtux/towerpanel" target="_blank" rel="noreferrer">TowerPanel</a></li>
				</ul>
			</div>
		</div>
	</section>

	<Divider borderStyle="border-dotted" opacity="opacity-50" />

	<!-- Row 2 -->
	<section class={cRowTwo}>
		<p class="text-xs">
			<a href="https://github.com/dumtux/towerpanel/blob/develop/LICENSE" target="_blank" rel="noreferrer">MIT License</a>
			<span class="opacity-10 mx-2">|</span>
			<a href="https://github.com/dumtux/towerpanel/graphs/contributors" target="_blank" rel="noreferrer">Contributors</a>
		</p>
		<div class="flex space-x-4">
			<a class="btn bg-[#7289da] text-white" href="https://linkedin.com/company/towersoftwareltd" target="_blank" rel="noreferrer">
				<SvgIcon name="linkedin" fill="fill-white" />
				<span class="hidden md:inline-block ml-2 text-white">LinkedIn</span>
			</a>
			<a class="btn bg-[#1da1f2] text-white" href="https://twitter.com/tower_software" target="_blank" rel="noreferrer">
				<SvgIcon name="twitter" fill="fill-white" />
				<span class="hidden md:inline-block ml-2 text-white">Twitter</span>
			</a>
			<a class="btn bg-[#6e5494] text-white" href="https://github.com/dumtux/omega2-4g-gateway" target="_blank" rel="noreferrer">
				<SvgIcon name="github" fill="fill-white" />
				<span class="hidden md:inline-block ml-2 text-white">Github</span>
			</a>
		</div>
	</section>
</div>
