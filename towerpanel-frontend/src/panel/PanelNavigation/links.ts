// Documentation AppBar Navigation

export const menuNavLinks: any = [
	{
		id: 'nav-devices',
		title: 'devices',
		list: [
			{ href: '/devices/gnss', label: 'GNSS', icon: 'gps' },
			{ href: '/devices/uhf', label: 'UHF Radio', icon: 'satellite' },
			{ href: '/devices/rs232', label: 'RS232', icon: 'rs232' },
			{ href: '/devices/rs485', label: 'RS485', icon: 'canbus' },
			// { href: '/devices/can', label: 'CAN', icon: 'canbus' },
		]
	},
	{
		id: 'nav-settings',
		title: 'Settings',
		list: [
			// { href: '/settings/network', label: 'Network', icon: 'lte' },
			{ href: '/settings/upgrade', label: 'System Upgrade', icon: 'cubes' },
		]
	},
	// {
	// 	id: 'nav-docs',
	// 	title: 'docs',
	// 	list: [
	// 		{ href: '/docs/why', label: 'Why TowerPanel' },
	// 		{ href: '/docs/gps', label: 'Precision GNSS' },
	// 	]
	// }
];
