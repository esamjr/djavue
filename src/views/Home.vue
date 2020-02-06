<template>
  <div class="home container mx-auto">
    <h1 class="text-5xl font-bold">Blog</h1>
    <div class="flex flex-wrap">
      <Post :item="article" v-for="article in articles" :key="article.id" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Post from "@/components/Post";

export default {
  name: "home",
  components: {
    Post
  },
  data() {
    return {
      articles: null,
    };
  },
  created() {
    this.fetchArticles();
  },
  methods: {
    async fetchArticles() {
      let endpoint = "http://127.0.0.1:5000/api/articles";

      let { data } = await axios.get(endpoint);
      this.articles = data;
      console.log(this.articles);
    }
  }
};
</script>
