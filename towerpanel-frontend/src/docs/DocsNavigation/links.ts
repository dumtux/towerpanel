// Documentation AppBar Navigation

export const menuNavLinks: any = [
	{
		id: 'nav-sensors',
		title: 'Sensors',
		list: [
			{ href: '/sensors/gnss', label: 'GNSS', icon: 'pen-ruler' },
			{ href: '/sensors/rs232', label: 'RS232', icon: 'pen-ruler' },
			{ href: '/sensors/rs485', label: 'RS485', icon: 'pen-ruler' },
			{ href: '/sensors/can', label: 'CAN', icon: 'pen-ruler' },
		]
	},
	{
		id: 'nav-settings',
		title: 'Settings',
		list: [
			{ href: '/settings/cellular', label: 'Cellular Network', icon: 'cubes' },
			{ href: '/settings/upgrade', label: 'System Upgrade', icon: 'cubes' },
		]
	},
	{
		id: 'nav-docs',
		title: 'docs',
		list: [
			{ href: '/docs/why', label: 'Why TowerPanel', icon: 'cubes' },
			{ href: '/docs/gps', label: 'Precision GNSS', icon: 'cubes' },
		]
	}
];
