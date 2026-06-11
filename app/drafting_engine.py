from core.logger import log


class DraftingEngine:

    def __init__(self):
        pass

    def generate_motion_outline(self, motion_type, facts, law):

        log(f"DRAFTING: {motion_type}")

        template = f"""
{motion_type.upper()} MOTION OUTLINE

I. INTRODUCTION
- Relief requested: {motion_type}

II. STATEMENT OF FACTS
{facts}

III. LEGAL STANDARD
{law}

IV. ARGUMENT
A. Governing law applies
B. Facts satisfy legal threshold
C. No genuine dispute exists

V. CONCLUSION
For the foregoing reasons, the Court should grant the motion.
"""

        return template
