import { SvelteComponentTyped } from "svelte";
declare const __propDef: {
    props: {
        [x: string]: any;
        devce_name?: string | undefined;
    };
    events: {
        [evt: string]: CustomEvent<any>;
    };
    slots: {
        default: {};
    };
};
export declare type WSTerminalProps = typeof __propDef.props;
export declare type WSTerminalEvents = typeof __propDef.events;
export declare type WSTerminalSlots = typeof __propDef.slots;
export default class WSTerminal extends SvelteComponentTyped<WSTerminalProps, WSTerminalEvents, WSTerminalSlots> {
}
export {};
