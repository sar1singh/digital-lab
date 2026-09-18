# WORKSPACE ROUTING & EXECUTION RULES

You are operating inside a multi-folder workspace containing:
- `engineering-foundations/`
- `lifeos-hq/`
- `digital-lab/`
- `agent-os/`

## OPERATIONAL RULES:
1. TARGET RESOLUTION: Analyze every request to determine which sub-folder it belongs to.
2. AMBIGUITY CHECK: If the user request does not explicitly mention a sub-folder or repo, PAUSE and ask: 
   "Which folder should I execute this task in? [engineering-foundations | lifeos-hq | digital-lab | agent-os]"
3. DO NOT modify any files until the target folder is either explicitly stated by the user or confirmed after asking.
4. SCOPED LOGIC: Once the target folder is resolved, inspect that specific folder's memory files or context before making file changes.
