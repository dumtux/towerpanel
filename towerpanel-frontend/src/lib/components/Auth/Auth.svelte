<script lang="ts">
    import { onMount } from 'svelte';
    import { is_authenticated } from "./store";
	import { Divider, Alert } from '@brainandbones/skeleton';

    let Monaco;
    let alert_auth_visible = true;

    let username: string = '';
    let password: string = '';

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
            <div class="col-span-4 card card-body space-y-4">
                <label for="name">
                    <span>Username</span>
                    <input type="text" id="username" bind:value={username} minlength="2" required>
                </label>
                <label for="name">
                    <span>Password</span>
                    <input type="text" id="password" bind:value={password} minlength="2" required>
                </label>
                <Divider />
                <button class="btn bg-primary-500 btn-base text-white" on:click={onLogin}>Login</button>
            </div>
        </div>
    </section>
</section>
