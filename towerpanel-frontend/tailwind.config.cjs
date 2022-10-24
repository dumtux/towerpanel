const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
	darkMode: 'class',
	content: [
		"./src/**/*.{html,js,svelte,ts}",
		"./node_modules/@brainandbones/skeleton/**/*.{html,js,svelte,ts}"
    ],
	theme: {
		extend: {
			fontFamily: {
				sans: ['Inter', ...defaultTheme.fontFamily.sans]
			}
		}
	},
	plugins: [
		require('@tailwindcss/forms'),
		require('./node_modules/@brainandbones/skeleton//tailwind/theme.cjs')
	]
};
