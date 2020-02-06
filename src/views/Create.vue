<template>
    <div class="home container mx-auto">
    <h1 class="text-5xl font-bold">Create Article</h1>
    <div class="flex flex-wrap">
        
    </div>
    <form-app></form-app>
  </div>
</template>

<script>
import FormCreateVue from '../components/FormCreate.vue'

export default {
    name: "create",
    components: {
        "form-app": FormCreateVue
    }
}
</script>