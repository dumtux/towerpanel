<script lang="ts">
	import JSEditor from '$lib/components/JSEditor/JSEditor.svelte';
	import { parseData } from '$lib/components/JSEditor/store';

	import { writable, type Writable } from "svelte/store";
	import { Divider, SlideToggle, TabGroup, Tab } from '@brainandbones/skeleton';
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';
	import { onMount, onDestroy } from 'svelte';

	const storeTab: Writable<string> = writable('console');
	let ws: WebSocket = null;

	const HOST = '192.168.0.48:8000'

	export let device_name: string = "test";
	export let default_baudrate: string = "9600";
	let baudrate = parseInt(default_baudrate);
	const BUADRATE_LIST = [4800, 9600, 19200, 38400, 57600, 115200];
	export let timeout = 4;
	const TIMEOUT_LIST = [1, 2, 4, 8, 16];
	export let rows = 16;

	const textEncoder = new TextEncoder();
	const textDecoder = new TextDecoder();
	let sendCommand = () => {};

	let alert_connection_visible = false;
	let alert_decoding_visible = false;
	const console_buffer: List<string> = [];
	for (let i = 0; i < rows; i++) {
		console_buffer.push("");
	}
	let console_text = console_buffer.join('\n');

	let gnss_command = "";

	// let is_monitoring: boolean = false;
	let is_monitoring = (e) => {
		console.log(e);
	};

	function onMonitoringChange(event: any) {
		console.log(is_monitoring);
	}

	function onSettingsChange(event: any) {
		fetch('http://' + HOST + '/bus/' + device_name, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ baudrate: baudrate, timeout: timeout, monitoring: is_monitoring })
		});
	}

	onMount(async () => {
		ws = new WebSocket("ws://" + HOST + "/ws/" + device_name);

		sendCommand = () => {
			console_buffer.push(device_name + ' ◄◄ ' + gnss_command);
			ws.send(JSON.stringify(Array.from(textEncoder.encode(gnss_command + '\r\n'))));
			gnss_command = "";
			if (console_buffer.length > rows) {
				console_buffer.shift();
			}
			console_text = console_buffer.join('\n');
		};

		ws.addEventListener("message", function (event) {
			const received_str = textDecoder.decode(new Uint8Array(JSON.parse(event.data)));
			console_buffer.push(device_name + ' ►► ' + received_str.replace("\r", "\\r").replace("\n", "\\n"));
			if (console_buffer.length > rows) {
				console_buffer.shift();
			}
			console_text = console_buffer.join('\n');
			$parseData(received_str);
		});

		ws.addEventListener("open", function (event) {
			alert_connection_visible = false;
		});

		ws.addEventListener("close", function (event) {
			alert_connection_visible = true;
		});
	});

	onDestroy(async () => {
		if (ws) {
			ws.close();
		}
		ws = null;
	});
</script>

<div>
	<TabGroup selected={storeTab}>
		<Tab value="console">Console</Tab>
		<Tab value="parser">Parser</Tab>
	</TabGroup>

	<!-- Conditionally display content -->
	{#if $storeTab === 'console'}
		<section class="space-y-4">
			<!-- <h1>GNSS</h1> -->
			<Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible={alert_connection_visible}>
				<span>
					Websocket connection is not established.
				</span>
			</Alert>
			<Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible={alert_decoding_visible}>
				<span>Failing to decode some bytes. Raw bytes data are shown. Try different baudrate.</span>
			</Alert>
			<section class="grid grid-cols-5 gap-4">
				<div class="col-span-4 card card-body space-y-4">
					<pre><code style="min-height: 28em; white-space: pre; word-break: normal; word-wrap: normal;">{console_text}</code></pre>
					<label for="gnss_command">
						<input type="text" id="gnss_command" bind:value={gnss_command} on:change={sendCommand} minlength="2" required placeholder="Type command and hit Enter to send.">
					</label>
				</div>
				<div class="card card-body space-y-4 min-w-min">
					<SlideToggle bind:checked={is_monitoring} on:change={onSettingsChange}>{is_monitoring ? 'Active' : 'Paused'}</SlideToggle>
					<Divider />
					<label>Baudrate</label>
					<select name="color" id="color" bind:value={baudrate} on:change={onSettingsChange}>
						{#each BUADRATE_LIST as value}
							<option value="{value}">{value} bps</option>
						{/each}
					</select>
					<Divider />
					<label>Read Timeout</label>
					<select name="color" id="color" bind:value={timeout} on:change={onSettingsChange}>
						{#each TIMEOUT_LIST as value}
							<option value="{value}">{value} s</option>
						{/each}
					</select>
				</div>
			</section>
		</section>
	{/if}

	{#if $storeTab === 'parser'}
		<JSEditor />
	{/if}

</div>
