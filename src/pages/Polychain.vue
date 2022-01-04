<template>
  <div class="content">
      <div v-for="asset in assets" :key="asset.name">
          {{asset[0]}}:{{asset[1]}}
        </div>
      
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
      .get('http://127.0.0.1:5000/polychain')
      .then(response => (this.assets = response.data))
  }
};
</script>
