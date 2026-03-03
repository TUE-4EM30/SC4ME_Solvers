<template>
  <footer class="footer">
    <img src="./images/tuelogo.svg" alt="TU/e Logo" class="logo" />
  </footer>
  <div class="page-number">
    {{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}
  </div>  
</template>

<style>
.footer {
  position: fixed;
  top: 10px;
  right: 10px;
  width: 80px; /* Adjust the width as needed */
}
.logo {
  width: 100%; /* Adjust the width as needed */
}
.page-number {
  position: fixed;
  bottom: 20px;
  right: 20px;
  font-size: 14px;
  opacity: 0.6;
}
</style>