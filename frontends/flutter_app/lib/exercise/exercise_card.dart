
import 'package:flutter/material.dart';

class ExerciseCard extends StatefulWidget {
  const ExerciseCard({super.key});

  @override
  State<StatefulWidget> createState() => _ExerciseCardState();
}

class _ExerciseCardState extends State {
  @override
  Widget build(BuildContext context) => Center(
    child: Row(
      children: [
        Image.asset(
          'assets/placeholders/exercise_placeholder.png',
          width: 64,
          height: 64,
        ),
        Flexible(
          child: Column(
            children: [
              const Text('Exercise Name'),
              const Text(
                'Exercise Description long long description and such such and jazz Exercise Description long long description and such such and jazz',
                maxLines: 4,
                overflow: TextOverflow.ellipsis,
              ),
            ],
          ),
        ),
      ],
    ),
  );
  
}