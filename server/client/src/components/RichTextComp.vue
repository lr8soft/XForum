<template>
  <div v-if="editable" style="border: 1px solid #ccc">
    <Toolbar
        style="border-bottom: 1px solid #ccc"
        :editor="editorRef"
        :defaultConfig="toolbarConfig"
        :mode="mode"
        v-if="editable"
    />
    <Editor
        style="height: 300px; overflow-y: hidden;"
        v-model="valueHtml"
        :defaultConfig="editorConfig"
        :mode="mode"
        @onCreated="handleCreated"
        @onChange="userInput"
    />
  </div>
  <div v-else>
    <Editor
        class="readonly-editor"
        v-model="valueHtml"
        :defaultConfig="editorConfig"
        :mode="mode"
        @onCreated="handleCreated"
        @onChange="userInput"
    />
  </div>
</template>

<script>
import '@wangeditor/editor/dist/css/style.css' // 引入 css

import {onBeforeUnmount, ref, shallowRef, defineEmits, watch, defineComponent} from 'vue'
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'

export default defineComponent({
  name: "RichTextComp",
  components: { Editor, Toolbar },
  props: {
    modelValue: String,
    editable: {
      type: Boolean,
      default: true
    }
  },
  emits:[
    'update:modelValue'
  ],
  setup(props, ctx) {
    // 编辑器实例，必须用 shallowRef
    const editorRef = shallowRef()

    // 内容 HTML
    const valueHtml = ref('<p></p>>')

    const toolbarConfig = {}
    const editorConfig = {}

    // 组件销毁时，也及时销毁编辑器
    onBeforeUnmount(() => {
      const editor = editorRef.value
      if (editor == null) return
      editor.destroy()
    })

    // 记录 editor 实例
    const handleCreated = (editor) => {
      editorRef.value = editor
    }

    // 父容器值更新就更新里面的
    watch(props,(newVal,oldVal) => {
      valueHtml.value = props.modelValue;
      editorConfig.readOnly = !props.editable
    },{immediate:true})

    const userInput = (editor)=>{
      ctx.emit('update:modelValue', valueHtml.value)
    }

    return {
      editorRef,
      valueHtml,
      mode: 'default',
      toolbarConfig,
      editorConfig,
      handleCreated,
      userInput
    };
  }
})
</script>

<style scoped>
.readonly-editor{
  --w-e-textarea-bg-color: transparent;
  --w-e-textarea-border-color: transparent;

  overflow-y: hidden;
}
</style>