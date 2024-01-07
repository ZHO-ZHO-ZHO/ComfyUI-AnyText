#from .AnyText.cldm.model import create_model, load_state_dict
from modelscope.pipelines import pipeline

class AnyTextNode_Zho:
  
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "A cake with colorful characters that reads \"EVERYDAY\"", "multiline": True}),
                "mode": ("text-generation",),  
                "image_count": ("INT", {"default": 2, "min": 1, "max": 10}),
                "ddim_steps": ("INT", {"default": 20, "min": 1, "max": 100}),
                "show_debug": ("BOOLEAN", {"default": True}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 99999999}),
                "draw_pos": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    CATEGORY = "✒️AnyText"
    FUNCTION = "run_anytext"

    def run_anytext(self, prompt, mode, image_count, ddim_steps, show_debug, seed, draw_pos):
        
        # Configure the pipeline for AnyText
        pipe = pipeline('my-anytext-task', model='damo/cv_anytext_text_generation_editing', model_revision='v1.1.1', use_fp16=True, use_translator=False)
        
        self.params = {
            "show_debug": show_debug,
            "image_count": image_count,
            "ddim_steps": ddim_steps,
        }

        input_data = {
            "prompt": prompt,
            "seed": seed,
            "draw_pos": draw_pos
        }

        results, rtn_code, rtn_warning, debug_info = pipe(input_data, mode=mode, **self.params)
        if rtn_code < 0:
            raise Exception(f"Error in AnyText pipeline: {rtn_warning}")

        return results

# Node class and display name mappings
NODE_CLASS_MAPPINGS = {
    "AnyTextNode_Zho": AnyTextNode_Zho
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "AnyTextNode_Zho": "✒️AnyText"
}
