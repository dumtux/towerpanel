// Documentation AppBar Navigation

export const menuNavLinks: any = [
	{
		id: 'nav-sensors',
		title: 'Sensors',
		list: [
			{ href: '/sensors/gnss', label: 'GNSS', icon: 'gps' },
			{ href: '/sensors/uhf', label: 'UHF Radio', icon: 'lte' },
			{ href: '/sensors/rs232', label: 'RS232', icon: 'rs232' },
			{ href: '/sensors/rs485', label: 'RS485', icon: 'canbus' },
			{ href: '/sensors/can', label: 'CAN', icon: 'canbus' },
		]
	},
	{
		id: 'nav-settings',
		title: 'Settings',
		list: [
			{ href: '/settings/cellular', label: 'Cellular Network', icon: 'lte' },
			{ href: '/settings/upgrade', label: 'System Upgrade', icon: 'cubes' },
		]
	},
	{
		id: 'nav-docs',
		title: 'docs',
		list: [
			{ href: '/docs/why', label: 'Why TowerPanel' },
			{ href: '/docs/gps', label: 'Precision GNSS' },
		]
	}
];
