<template>
  <div class="home container mx-auto">
    <h1 class="text-5xl font-bold">Blog</h1>
    <div class="flex flex-wrap">
      <Post :article="article" v-for="article in articles" :key="article.id" />
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
      endpoint: "/api/v1/articles/",
      articles: null
    };
  },
  created() {
    this.fetchArticles();
  },
  methods: {
    async fetchArticles() {
      let { data } = await axios.get(this.endpoint);

      this.articles = data;
    }
  }
};
</script>
