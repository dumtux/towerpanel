<script>
    import { readable } from "svelte/store";

    export const socketStore = readable({}, set => {
        const socket = new WebSocket("ws://192.168.0.6:8000/ws");

        socket.addEventListener("message", function (event) {
            const data = JSON.parse(event.data);
            set(data);
        });

        return () => { socket.close() };
    });
</script>
