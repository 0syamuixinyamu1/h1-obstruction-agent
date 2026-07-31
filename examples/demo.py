from h1_agent import H1ObstructionAgent


def main() -> None:
    agent = H1ObstructionAgent(threshold=0.35)

    inputs = [
        "The system gave two incompatible explanations for the same event.",
        "The system again gave incompatible explanations and silently merged them.",
    ]

    for text in inputs:
        result = agent.process(text)
        print(f"\nINPUT: {text}")
        print(f"Detected obstructions: {len(result.obstructions)}")
        for obstruction in result.obstructions[:3]:
            print(
                f"- {obstruction.obstruction_id} "
                f"score={obstruction.residual_score:.3f} "
                f"cycle={obstruction.projections}"
            )

    print(f"\nTotal memory items: {len(agent.memory.items)}")


if __name__ == "__main__":
    main()
