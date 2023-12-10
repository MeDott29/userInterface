The steps for creating and utilizing OpenAI's function calling features are something like the following:

define code/function to be used by assistant
ask the assistant a question for which it must use the function to retrieve an answer
the assistant will reply with arguments corresponding to a previously defined and described function
write code that passes the response arguments to the proper function

(at this point, the results of the function could be printed to terminal or returned to the model, etc.)
