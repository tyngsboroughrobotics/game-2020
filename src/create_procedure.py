from botball.core import step, Procedure

@step(name="Temporary")
def temporary():
    print("TEMP")

procedure = Procedure(name="Create Temp", steps=[
    temporary,
])
