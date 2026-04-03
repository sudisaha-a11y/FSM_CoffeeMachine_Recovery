# Coffee Machine FSM Architecture

## Overview
This document describes the architecture of the Coffee Machine Recovery framework using Finite State Machine (FSM) design pattern.

## Components

### States
- **Idle State**: Machine is ready and waiting for user input
- **Brewing State**: Machine is actively brewing coffee
- **Error State**: Machine has encountered an error

### Transitions
- Idle → Brewing: User initiates brew process
- Brewing → Idle: Brew cycle completes
- Any State → Error: Error condition detected
- Error → Idle: Error is resolved

## Design Principles
- Modular design for scalability
- Comprehensive error handling
- State isolation and independence
