export enum PanelFeature {
	Element = 'Tailwind Element',
	Component = 'Svelte Component',
	Action = 'Svelte Action',
	Utility = 'Utility'
}

interface PanelShellLinks {
	label: string;
	url: string;
}

export interface PanelShellSettings {
	/** Enum: Documentation | Element | Component | Action | Utility */
	feature: PanelFeature;
	/** The feature name. */
	name: string;
	/** The feature description */
	description: string;
	/** List of import alias names. */
	imports?: string[];
	/** List of import Typescript interface imports. */
	types?: string[];
	/** List of stylesheets that include the required styles. */
	stylesheetIncludes?: string[];
	/** List of CSS import paths (partials) */
	stylesheets?: string[];
	/** The NPM package this feature belongs to. */
	package?: {
		/** Package Name */
		name: string;
		/** Package URL */
		url: string;
	};
	/** Specify the source path (partials) */
	source: string;
	/** Provide the GitHub documentation route path (partial) */
	docs?: string;
	/** Provide list of depedency links.  */
	dependencies?: PanelShellLinks[];
	/** When enabled, renames tab "Props" to "Params" for Svelte Actions */
	parameters?: boolean;
}

export interface PanelShellTable {
	/** Provide a semantic label. */
	label?: string;
	/** Provide HTML for description region. */
	description?: string;
	/** Provide the table headings. */
	headings?: string[];
	/** Provide the table source data. */
	source?: string[][];
	/** WAI-ARIA APG page link. */
	aria?: string;
}
