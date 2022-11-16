<script lang="ts">
    import { onMount } from 'svelte';
    import { is_authenticated } from "./store";
	import Alert from '@brainandbones/skeleton/components/Alert/Alert.svelte';

    let Monaco;
    let alert_auth_visible = true;

    function onLogin() {}

    onMount(async () => {
        // @ts-ignore
    });
</script>

<section class="space-y-4">
    <Alert background="bg-warning-500/30" border="border-l-4 border-warning-500" visible={alert_auth_visible}>
        <span>
            Authenticatin failed.
        </span>
    </Alert>
    <section class="flex justify-center">
        <div class="col-span-1 card card-body space-y-4 flex justify-center">
            <button class="btn bg-primary-500 btn-base text-white" on:click={onLogin}>Login</button>
        </div>
    </section>
</section>
