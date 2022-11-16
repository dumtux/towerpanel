<script lang="ts">
	import { Divider, RangeSlider } from '@brainandbones/skeleton';
	import WSTerminal from '$lib/components/WSTerminal/WSTerminal.svelte';

	let module: string = "TR4+";
	let serial_number: string = "0123456789";
	let rssi: number = -116.0;

	const CHANEL_SPACING_LIST = [12.5, 20.0, 25];
	let channel_spacing: number = CHANEL_SPACING_LIST[0];
	const TX_POWER_LIST = [500.0, 1000.0];
	let tx_power: number = TX_POWER_LIST[0];
	const PROTOCOL_LIST = ["TRIMTALK", "TRANSEOT", "SOUTH", "SOUTH"];
	let protocol: string = PROTOCOL_LIST[0];

	const MIN_FREQENcY = 403.00000;
	const MAX_FREQENcY = 473.00000;
	let rx_frequency: number = MIN_FREQENcY;
	let tx_frequency: number = MIN_FREQENcY;

	function onSettingsChange(event: any) {
		console.log("nothing");
	};

	function formatFrequency(value: number) {
		return (Math.round(value * 1000) / 1000).toFixed(3);
	}
</script>

<div class="page-container">
	<section class="card card-body space-y-4">
		<div class="grid grid-cols-3 gap-4">
			<div>
				<label>Module</label>
				<input type="text" bind:value={module} readonly />
			</div>
			<div>
				<label>SN</label>
				<input type="text" bind:value={serial_number} readonly />
			</div>
			<div>
				<label>RSSI</label>
				<input type="text" bind:value={rssi} readonly />
			</div>
		</div>
	</section>
	<section class="card card-body space-y-4">
		<div class="justify-center items-center">
			<div class="flex justify-between items-center">
				<div>RX Frequency</div>
				<div class="text-xs">{MAX_FREQENcY}</div>
			</div>
			<RangeSlider bind:value={rx_frequency} min={MIN_FREQENcY} max={MAX_FREQENcY} step={0.025} ticked></RangeSlider>
			<p class="text-center"><code>{formatFrequency(rx_frequency)}</code> MHz</p>
		</div>
		<div class="justify-center items-center">
			<div class="flex justify-between items-center">
				<div>TX Frequency</div>
				<div class="text-xs">{MAX_FREQENcY}</div>
			</div>
			<RangeSlider bind:value={tx_frequency} min={MIN_FREQENcY} max={MAX_FREQENcY} step={0.025} ticked></RangeSlider>
			<p class="text-center"><code>{formatFrequency(tx_frequency)}</code> MHz</p>
		</div>
		<div class="grid grid-cols-3 gap-4">
			<div>
				<label>Channel Spacing</label>
				<select name="channel_spacing" id="channel_spacing" bind:value={channel_spacing} on:change={onSettingsChange}>
					{#each CHANEL_SPACING_LIST as value}
						<option value="{value}">{value} kHz</option>
					{/each}
				</select>
			</div>
			<div>
				<label>TX Power</label>
				<select name="tx_power" id="tx_power" bind:value={tx_power} on:change={onSettingsChange}>
					{#each TX_POWER_LIST as value}
						<option value="{value}">{value} mW</option>
					{/each}
				</select>
			</div>
			<div>
				<label>Protocol</label>
				<select name="protocol" id="protocol" bind:value={protocol} on:change={onSettingsChange}>
					{#each PROTOCOL_LIST as value}
						<option value="{value}">{value}</option>
					{/each}
				</select>
			</div>
		</div>
		<Divider />
		<button class="btn bg-primary-500 btn-base text-white">Update</button>
		<button class="btn bg-primary-500 btn-base text-white" disabled>Save Permanently</button>
	</section>

	<WSTerminal device_name="uhf" default_baudrate="19200" />
</div>
