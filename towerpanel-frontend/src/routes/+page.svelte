<script lang="ts">
	// Components
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';
	import Avatar from '@brainandbones/skeleton/components/Avatar/Avatar.svelte';
	import SvgIcon from '$lib/components/SvgIcon/SvgIcon.svelte';
</script>

<div>
	<!-- Alert: Beta -->
	<Alert>
		<svelte:fragment slot="lead">🚧</svelte:fragment>
		<span>TowerPanel is available as a public repository. If you encounter issues please report them on GitHub.</span>
		<svelte:fragment slot="trail">
			<a href="https://github.com/dumtux/towerpanel/issues" target="_blank" rel="noreferrer" class="btn btn-ghost">Report Issue</a>
		</svelte:fragment>
	</Alert>

	<div class="container max-w-[1200px] mx-auto px-4 py-10 md:py-20 space-y-20">
		<!-- Hero -->
		<header>
			<div class="space-y-6">
				<h2 class="text-4xl md:text-6xl lg:text-7xl">Operating Panel Webapp for TowerController III</h2>
				<p class="text-xl">
					TowerPanel allows you to configure and monitor sensor data on web interfaces using the <a href="hhttps://github.com/dumtux/omega2-4g-gateway" target="_blank" rel="noreferrer">TowerController III</a>
					+ <a href="https://github.com/dumtux/towerwrt" target="_blank" rel="noreferrer">TowerWrt</a>.
				</p>
				<nav class="flex space-x-4">
					<a href="/sensors/gnss" class="btn btn-lg btn-filled-primary"><span class="text-white">Go to Workspace</span></a>
					<a href="/docs/why" class="btn btn-lg btn-ghost">Why TowerPanel</a>
				</nav>
			</div>
		</header>

		<!-- Features -->
		<section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
			<h2 class="sr-only">Features</h2>
			<div class="card card-body space-y-4">
				<div class="bg-accent-500 w-14 aspect-square flex justify-center items-center rounded-token shadow">
					<SvgIcon name="screwdriver" fill="fill-white" width="w-8" height="h-8" />
				</div>
				<h4>Adaptive Sensor Bus</h4>
				<p>Most common sensor interfaces are ready. CAN bus with CANOpen support, RS485 with Modbus support and RS232</p>
			</div>
			<div class="card card-body space-y-4">
				<div class="bg-primary-500 w-14 aspect-square flex justify-center items-center rounded-token shadow">
					<SvgIcon name="connectivity" fill="fill-white" width="w-8" height="h-8" />
				</div>
				<h4>Connectivity</h4>
				<p>Supports Ethernet, Wi-Fi, LTE and UHF for establishing the most reliable Internet connection ever.</p>
			</div>
			<div class="card card-body space-y-4">
				<div class="bg-orange-500 w-14 aspect-square flex justify-center items-center rounded-token shadow">
					<SvgIcon name="openwrt" fill="fill-white" width="w-10" height="h-10" />
				</div>
				<h4>OpenWrt</h4>
				<p>
					Tightly coupled with OpenWrt, the de-facto standard operating system for network routers.
					<a href="https://github.com/dumtux/towerwrt" target="_blank" rel="noreferrer">TowerWrt</a> is just a minimum customized OpenWrt.
				</p>
			</div>
			<div class="card card-body space-y-4">
				<div class="bg-sky-500 w-14 aspect-square flex justify-center items-center rounded-token shadow">
					<SvgIcon name="python" fill="fill-white" width="w-10" height="h-10" />
				</div>
				<h4>Concurrent Python</h4>
				<p>Everything under thingle-threaded Python, asynchronous non-blocking hardware I/O operations.</p>
			</div>
		</section>

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
