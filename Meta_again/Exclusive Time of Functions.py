class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        execution_time = [0]*n

        prev_time = 0

        call_stack = []


        for log in logs:

            func_id,call_type,timestamp = log.split(":")

            func_id = int(func_id)
            timestamp = int(timestamp)

            if call_type == "start":

                if call_stack:
                    execution_time[call_stack[-1]]+=timestamp-prev_time

                prev_time = timestamp
                call_stack.append(func_id)
            
            else:

                execution_time[call_stack.pop()]+=timestamp-prev_time+1
                prev_time = timestamp+1
        
        return execution_time



        
