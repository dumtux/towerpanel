<script lang="ts">
	import { writable, type Writable } from "svelte/store";
	import { Divider, RadioGroup, RadioItem, ListBox, ListBoxItem } from '@brainandbones/skeleton';
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';

    import { diagRouting, diagRoutingWifiAP } from '$lib/components/NetworkConfig/diag.js';

    const store_ethernet_mode: Writable<string> = writable('static-ip');

    const store_uplink_mode: Writable<string> = writable("ethernet");
    const store_downlink_mode: Writable<string> = writable("ethernet");

    let static_ip_address_0 = 0;
    let static_ip_address_1 = 0;
    let static_ip_address_2 = 0;
    let static_ip_address_3 = 0;

    let gateway_address_0 = 0;
    let gateway_address_1 = 0;
    let gateway_address_2 = 0;
    let gateway_address_3 = 0;

    let dns1_address_0 = 0;
    let dns1_address_1 = 0;
    let dns1_address_2 = 0;
    let dns1_address_3 = 0;

    let dns2_address_0 = 0;
    let dns2_address_1 = 0;
    let dns2_address_2 = 0;
    let dns2_address_3 = 0;

</script>

<div class="page-container">
    <section class="grid grid-cols-2 lg:grid-cols-2 gap-4">
        <div class="space-y-4">
            <section class="card">
                <header class="card-header"><h3>Ethernet</h3></header>
                <div class="card-body">
                    <RadioGroup selected={store_ethernet_mode}>
                        <RadioItem value="static-ip">Static IP</RadioItem>
                        <RadioItem value="dhcp-client">DHCP Client</RadioItem>
                        <RadioItem value="dhcp-server">DHCP Server</RadioItem>
                    </RadioGroup>
                    <div class="grid grid-cols-5 gap-2 space-y-4">
                        <label>IP Address</label>
						<input class="rounded-none text-center" type="number" bind:value={static_ip_address_0} />
						<input class="rounded-none text-center" type="number" bind:value={static_ip_address_1} />
						<input class="rounded-none text-center" type="number" bind:value={static_ip_address_2} />
						<input class="rounded-none text-center" type="number" bind:value={static_ip_address_3} />
                    </div>
                    <div class="grid grid-cols-5 gap-2 space-y-4">
                        <label>Gateway</label>
						<input class="rounded-none text-center" type="number" bind:value={gateway_address_0} />
						<input class="rounded-none text-center" type="number" bind:value={gateway_address_1} />
						<input class="rounded-none text-center" type="number" bind:value={gateway_address_2} />
						<input class="rounded-none text-center" type="number" bind:value={gateway_address_3} />
                    </div>
                    <div class="grid grid-cols-5 gap-2 space-y-4">
                        <label>DNS 1</label>
						<input class="rounded-none text-center" type="number" bind:value={dns1_address_0} />
						<input class="rounded-none text-center" type="number" bind:value={dns1_address_1} />
						<input class="rounded-none text-center" type="number" bind:value={dns1_address_2} />
						<input class="rounded-none text-center" type="number" bind:value={dns1_address_3} />
                    </div>
                    <div class="grid grid-cols-5 gap-2 space-y-4">
                        <label>DNS 2</label>
						<input class="rounded-none text-center" type="number" bind:value={dns2_address_0} />
						<input class="rounded-none text-center" type="number" bind:value={dns2_address_1} />
						<input class="rounded-none text-center" type="number" bind:value={dns2_address_2} />
						<input class="rounded-none text-center" type="number" bind:value={dns2_address_3} />
                    </div>
                </div>
                <footer class="card-footer space-y-4">
                    <Divider />
                    <button class="btn bg-primary-500 btn-base text-white">Apply & Save</button>
                </footer>
            </section>
        </div>

        <div class="space-y-4">
            <section class="card">
                <header class="card-header"><h3>Cellular</h3></header>
                <div class="card-body"></div>
                <footer class="card-footer space-y-4">
                    <div class="grid grid-cols-2 gap-4">
                        <div class="spce-y-4">
                            <label>APN</label>
                            <input class="rounded-none text-center" type="text" />
                        </div>
                        <div class="spce-y-4">
                            <label>Protocol</label>
                            <input class="rounded-none text-center" type="text" />
                        </div>
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="spce-y-4">
                            <label>Password</label>
                            <input class="rounded-none text-center" type="text" />
                        </div>
                        <div class="spce-y-4">
                            <label>IP Type</label>
                            <input class="rounded-none text-center" type="text" />
                        </div>
                    </div>
                    <Divider />
                    <button class="btn bg-primary-500 btn-base text-white">Apply & Save</button>
                </footer>
            </section>

            <section class="card">
                <header class="card-header"><h3>Wi-Fi</h3></header>
                <div class="card-body"></div>
                <footer class="card-footer space-y-4">
                    <Divider />
                    <button class="btn bg-primary-500 btn-base text-white">Apply & Save</button>
                </footer>
            </section>

            <!-- <section class="card">
                <header class="card-header"><h3>Routing</h3></header>
                <div class="card-body">
                    <pre class="asciiart"><code>{diagRouting}</code></pre>
                </div>
            </section> -->
        </div>
    </section>
</div>

<style>
    pre.asciiart, pre.asciiart > code {
        line-height: 1em;
        font-size: 1em;
        font-family: monospace;
        background-color: transparent;
        white-space: none;
        text-align: left;
    }
</style>