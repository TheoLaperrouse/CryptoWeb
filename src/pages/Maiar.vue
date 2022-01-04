<template>
  <div class="content">
      {{assets}}
  </div>
</template>

<script>
import axios from 'axios'
export default {
  components: {
  },
  data() {
      return {
          assets : null
      }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:5000/maiar')
      .then(response => (this.assets = response))
  }
};
</script>
