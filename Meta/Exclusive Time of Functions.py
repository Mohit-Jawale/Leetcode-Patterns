class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:



        execution_times = [0]*n

        call_stack = []

        prev_timestamp = 0

        for log in logs:
            func_id,call_type,timestamp = log.split(':')

            func_id = int(func_id)
            timestamp = int(timestamp)

            if call_type=='start':
                if call_stack:
                    execution_times[call_stack[-1]] += timestamp - prev_timestamp

                prev_timestamp = timestamp
                call_stack.append(func_id)
            else:

                 execution_times[call_stack.pop()] += timestamp - prev_timestamp + 1

                 prev_timestamp = timestamp + 1
        
        return execution_times







        
