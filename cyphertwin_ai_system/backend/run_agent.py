from agents.agent_runner import run_flow 
from langflow.utils.flow import load_flow_from_file 
from langflow_interface.run import run_flow 

def main():
    flow_file = 'agents/daily_checks.flow'
    # Load flow config from file 
    flow = load_flow_from_file(flow_file)
    
    # Define inputs vaues if needed
    input_data = {'input' : 'Run daily cyber health check.'}

    # Run the flow 
    results = run_flow(flow=flow inputs=inputs_data)

    print('Flow output: ')
    print(results)

if __name__ == '__main__':
    main()

