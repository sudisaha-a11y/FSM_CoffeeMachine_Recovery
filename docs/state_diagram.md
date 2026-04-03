# Coffee Machine State Diagram

```
         ┌─────────────────────────┐
         │                         │
         │    [Idle State]         │
         │                         │
         └──────────┬──────────────┘
                    │
                    │ User starts brew
                    ↓
         ┌─────────────────────────┐
         │                         │
         │   [Brewing State]       │
         │                         │
         └──────────┬──────────────┘
                    │
                    │ Brew complete
                    ↓
         ┌─────────────────────────┐
         │                         │
         │    [Idle State]         │
         │                         │
         └─────────────────────────┘

         Any State → [Error State] on error condition
         [Error State] → [Idle State] on error recovery
```

## State Descriptions

### Idle State
- Machine is powered on and ready
- Waiting for user input to start brewing
- All systems operational

### Brewing State
- Heating water
- Extracting coffee
- Cannot accept new commands

### Error State
- System malfunction detected
- Requires intervention or reset
- All brewing stopped
