<script>
  import towerLogo from './assets/tower.png'
  import Counter from './lib/Counter.svelte'
</script>

<main>
  <div>
    <a href="http://www.towersoftwareltd.com/" target="_blank"> 
      <img src={towerLogo} class="logo svelte" alt="TowerSoftware Logo" />
    </a>
  </div>
  <h1>TowerPanel</h1>

  <div class="card">
    <Counter />
  </div>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
</style>
