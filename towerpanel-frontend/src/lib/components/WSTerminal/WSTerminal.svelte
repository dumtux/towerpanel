<script lang="ts">
	import { writable, type Writable } from "svelte/store";
	import { Divider, TabGroup, Tab } from '@brainandbones/skeleton';
	import ListBox from '@brainandbones/skeleton/components/ListBox/ListBox.svelte';
	import ListBoxItem from '@brainandbones/skeleton/components/ListBox/ListBoxItem.svelte';
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';

	export let device_name = "test";
	let rows = 16

	const GNSS_DEFAULT_BAUDRATE = 19200;

	let alert_decoding_visible = false;
	let console_text = "";
	const console_buffer: List<string> = [];
	for (let i = 0; i < rows; i++) {
		console_buffer.push("_");
	}

	const textEncoder = new TextEncoder();
	const textDecoder = new TextDecoder();

	const baudrate: Writable<number> = writable(GNSS_DEFAULT_BAUDRATE);
	let gnss_command = "";

	const ws = new WebSocket("ws://192.168.0.6:8000/ws/" + device_name);

	function sendCommand() {
		console_buffer.push('Vega28 ◄◄ ' + gnss_command);
		ws.send(JSON.stringify(Array.from(textEncoder.encode(gnss_command + '\r\n'))));
		gnss_command = "";
		if (console_buffer.length > rows) {
			console_buffer.shift();
		}
		console_text = console_buffer.join('\n');
	}

	ws.addEventListener("message", function (event) {
		const received_str = textDecoder.decode(new Uint8Array(JSON.parse(event.data)));
		console_buffer.push('Vega28 ►► ' + received_str.replace("\r", "\\r").replace("\n", "\\n"));
		if (console_buffer.length > rows) {
			console_buffer.shift();
		}
		console_buffer[0] = " ";
		console_text = console_buffer.join('\n');
    });
</script>

<div class="page-container">
	<!-- Install -->
	<section class="space-y-4">
		<!-- <h1>GNSS</h1> -->
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
			<div class="card card-body space-y-4">
				<ListBox selected="{baudrate}" label="Baudrate">
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
	</section>

	<Divider />

</div>
