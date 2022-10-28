<script>
    import * as THREE from 'three';
    import NET from 'vanta/dist/vanta.net.min';

    function vanta(node) {
        NET({
            el: node,
            THREE: THREE,
			mouseControls: true,
  touchControls: true,
  gyroControls: false,
  minHeight: 200.00,
  minWidth: 200.00,
  scale: 1.00,
  scaleMobile: 1.00,
  color: 0x7accfe,
  backgroundColor: 0x010f18
		})
    }

</script>

<div use:vanta/>