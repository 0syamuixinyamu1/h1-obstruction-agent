# Theory Note

## Operational hypothesis

A system exhibits structural self-monitoring when it can:

1. construct multiple local descriptions of the same situation;
2. detect when those descriptions cannot be globally reconciled;
3. preserve the unresolved incompatibility across time;
4. allow that preserved incompatibility to alter later inference.

## Approximation used here

For projection conditions `i`, `j`, and `k`, the prototype computes directed discrepancy vectors:

```text
c_ij, c_jk, c_ki
```

The cycle residual is:

```text
||c_ij + c_jk + c_ki||
```

A large residual is treated as an operational gluing obstruction.

This resembles a cocycle-consistency test, but it is not yet a mathematically complete sheaf-cohomology pipeline. A full version would require explicit stalks, restriction maps, cochain complexes, and filtration-indexed persistence calculations.
