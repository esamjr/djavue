<template>
    <div class="home container mx-auto">
    <h1 class="text-5xl font-bold">Edit Article</h1>
    <div class="flex flex-wrap">
        
    </div>
    <form-app></form-app>
  </div>
</template>

<script>
import FormEditVue from '../components/FormEdit.vue'

export default {
    name: "edit",
    components: {
        "form-app": FormEditVue
    }
}
</script>