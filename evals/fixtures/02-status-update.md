The parser refactor landed this morning. Coverage is at 84 percent, up from 71. The remaining gap is the error path in the tokenizer, which I'll pick up next sprint.

Two things changed for consumers. The parse function now returns a result object rather than raising, and the legacy entry point is deprecated but still present until the next major version.

Deployment is scheduled for Thursday.
