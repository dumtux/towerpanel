<script lang="ts">
	import WSTerminal from '$lib/components/WSTerminal/WSTerminal.svelte';
</script>

<div class="page-container">
	<WSTerminal device_name="gps" default_baudrate="115200" />
</div>
