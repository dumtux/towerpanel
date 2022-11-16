import { writable } from 'svelte/store';

let is_authenticated = writable((d) => {});

export {is_authenticated}
