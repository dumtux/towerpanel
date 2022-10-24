<script lang="ts">
	import { storeFramework } from '$panel/stores';
	import { Divider, TabGroup, Tab } from '@brainandbones/skeleton';
	import CodeBlock from '@brainandbones/skeleton/utilities/CodeBlock/CodeBlock.svelte';
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';
	import ListBox from '@brainandbones/skeleton/components/ListBox/ListBox.svelte';
	import ListBoxItem from '@brainandbones/skeleton/components/ListBox/ListBoxItem.svelte';
	import { writable, type Writable } from "svelte/store";
	import SlideToggle from '@brainandbones/skeleton/components/SlideToggle/SlideToggle.svelte';

	const TERMINAL_MAX_ROWS = 10;
	const GNSS_DEFAULT_BAUDRATE = 19200;

	let alert_decoding_visible = false;
	let downstream_data = " ";
	let upstream_data = " ";

	const baudrate: Writable<number> = writable(GNSS_DEFAULT_BAUDRATE);
	let gnss_command = "";
	const gnss_config = {
		baudrate: GNSS_DEFAULT_BAUDRATE,
		ethernet_enabled: false
	};

    const ws = new WebSocket("ws://192.168.0.6:8000/ws");
	const rx_buffer: List<string> = [];

    ws.addEventListener("message", function (event) {
      const json_rx = JSON.parse(event.data);
	  if (json_rx["gnss_rx_type"] == "string") {
		  rx_buffer.push(json_rx["gnss_rx"].replace("\r\n", "\n"));
		  alert_decoding_visible = false;
	  } else if (json_rx["gnss_rx_type"] == "bytes") {
		  rx_buffer.push(json_rx["gnss_rx"].slice(2, json_rx["gnss_rx"].length-1) + '\n');
		  alert_decoding_visible = true;
	  } else {
		  rx_buffer.push(json_rx["gnss_rx"]);
		  alert_decoding_visible = true;
	  }
	  if (rx_buffer.length > TERMINAL_MAX_ROWS) {
		  rx_buffer.shift();
	  }
	  downstream_data = rx_buffer.join('');
    });
</script>

<div class="page-container">
	<!-- Install -->
	<section class="space-y-4">
		<h1>GNSS</h1>
		<!-- Tabs -->
		<TabGroup selected={storeFramework}>
			<Tab value="uart">Console</Tab>
			<Tab value="config">Config</Tab>
			<Tab value="webui">WebUI</Tab>
		</TabGroup>
		{#if $storeFramework === 'uart'}
			<!-- <label for="baudrate">
				<span>Baudrate</span>
				<select name="baudrate" id="baudrate" bind:value={baudrate}>
					<option value="4800">4800 bps</option>
					<option value="9600">9600 bps</option>
					<option value="14400">14400 bps</option>
					<option value="19200">19200 bps</option>
					<option value="38400">38400 bps</option>
					<option value="57600">57600 bps</option>
					<option value="115200">115200 bps</option>
				</select>
			</label> -->
			<section class="grid grid-cols-1 lg:grid-cols-2 gap-4">
				<div class="card card-body space-y-4">
					<h2>TowerController ► Vega28</h2>
					<CodeBlock
						language="plaintext"
						code="{upstream_data}"
					/>
					<label for="gnss_command">
						<input type="text" id="gnss_command" bind:value={gnss_command} minlength="2" required placeholder="Type command and hit Enter to send.">
					</label>
				</div>
				<div class="card card-body space-y-4">
					<h2>TowerController ◄ Vega28</h2>
					<Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible={alert_decoding_visible}>
						<span>Failing to decode some bytes. Raw bytes data are shown. Check if UART baudrate correct.</span>
					</Alert>
					<CodeBlock
						language="plaintext"
						code={downstream_data}
					/>
				</div>
			</section>
		{:else if $storeFramework === 'webui'}
			<iframe class="tower-webui" src="http://192.168.0.25/index.cgi"></iframe>
		{:else if $storeFramework === 'config'}
			<section class="grid grid-cols-1 lg:grid-cols-3 gap-4">
				<div class="card card-body space-y-4">
					<h2>Status</h2>
				</div>
				<div class="card card-body space-y-4">
					<h2>Ethernet</h2>

					<div class="card card-body flex justify-center items-center space-x-4">
						<SlideToggle size="md" bind:checked={gnss_config.ethernet_enabled}>Ethernet</SlideToggle>
					</div>
					<div class="card card-body flex justify-center items-center space-x-4">
						<SlideToggle disabled label="Toggle Disabled">DHCP</SlideToggle>
					</div>
					<div class="card card-body flex justify-center items-center space-x-4">
						<SlideToggle disabled label="Toggle Disabled">WebUI</SlideToggle>
					</div>
				</div>
				<div class="card card-body space-y-4">
					<h2>UART</h2>
					<ListBox selected="{baudrate}">
						<ListBoxItem value={4800}>4800 bps</ListBoxItem>
						<ListBoxItem value={9600}>9600 bps</ListBoxItem>
						<ListBoxItem value={14400}>14400 bps</ListBoxItem>
						<ListBoxItem value={19200}>19200 bps</ListBoxItem>
						<ListBoxItem value={38400}>38400 bps</ListBoxItem>
						<ListBoxItem value={57600}>57600 bps</ListBoxItem>
						<ListBoxItem value={115200}>115200 bps</ListBoxItem>
					</ListBox>
				</div>
			</section>
		{/if}
	</section>

	<Divider />

</div>

<style>
	iframe.tower-webui {
		width: 100%;
		height: 50em;
	}
</style>