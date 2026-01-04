#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Brain Root Components

Tests for: Observer, Judge, Learner, A/B Tester, Model Optimizer, Self-Improver
"""

import pytest
import json
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent.parent / "tools" / "brain"))


class TestObserver:
    """Tests for Observer component."""
    
    def test_load_observer_log_creates_default(self, tmp_path):
        """Test that loading non-existent log creates default."""
        from observer import load_observer_log, get_observer_log_path
        
        with patch('observer.get_observer_log_path', return_value=tmp_path / "test-log.json"):
            log = load_observer_log()
            assert log["status"] == "ACTIVE"
            assert log["halted"] == False
            assert log["violations"] == []
    
    def test_halt_sets_status(self, tmp_path):
        """Test that halt sets status correctly."""
        from observer import halt, load_observer_log, get_observer_log_path
        
        log_path = tmp_path / "test-log.json"
        with patch('observer.get_observer_log_path', return_value=log_path):
            result = halt("Test error")
            assert result["status"] == "HALTED"
            assert result["reason"] == "Test error"
    
    def test_resume_clears_halt(self, tmp_path):
        """Test that resume clears halt state."""
        from observer import halt, resume, get_observer_log_path
        
        log_path = tmp_path / "test-log.json"
        with patch('observer.get_observer_log_path', return_value=log_path):
            halt("Test error")
            result = resume()
            assert result["status"] == "ACTIVE"


class TestJudge:
    """Tests for Judge component."""
    
    def test_load_scores_creates_default(self, tmp_path):
        """Test that loading non-existent scores creates default."""
        from judge import load_scores, get_scores_path
        
        with patch('judge.get_scores_path', return_value=tmp_path / "test-scores.json"):
            scores = load_scores()
            assert scores["scores"] == []
            assert scores["passThreshold"] == 6
    
    def test_set_threshold(self, tmp_path):
        """Test setting pass threshold."""
        from judge import set_threshold, get_scores_path
        
        scores_path = tmp_path / "test-scores.json"
        with patch('judge.get_scores_path', return_value=scores_path):
            result = set_threshold(8)
            assert result["threshold"] == 8


class TestLearner:
    """Tests for Learner component."""
    
    def test_load_learner_log_creates_default(self, tmp_path):
        """Test that loading non-existent log creates default."""
        from learner import load_learner_log, get_learner_log_path
        
        with patch('learner.get_learner_log_path', return_value=tmp_path / "test-log.json"):
            log = load_learner_log()
            assert log["learnings"] == []
            assert log["autoLearnEnabled"] == True


class TestABTester:
    """Tests for A/B Tester component."""
    
    def test_create_test(self, tmp_path):
        """Test creating a new A/B test."""
        from ab_tester import create_test, load_tests, get_tests_path
        
        tests_path = tmp_path / "test-tests.json"
        with patch('ab_tester.get_tests_path', return_value=tests_path):
            test = create_test("Test description")
            assert test["id"] == "TEST-001"
            assert test["status"] == "PENDING"
            assert test["description"] == "Test description"


class TestModelOptimizer:
    """Tests for Model Optimizer component."""
    
    def test_analyze_task_simple(self):
        """Test simple task analysis."""
        from model_optimizer import analyze_task
        
        result = analyze_task("format the code")
        assert result["taskType"] == "simple"
    
    def test_analyze_task_complex(self):
        """Test complex task analysis."""
        from model_optimizer import analyze_task
        
        result = analyze_task("refactor the authentication architecture")
        assert result["taskType"] == "complex"
    
    def test_recommend_model(self, tmp_path):
        """Test model recommendation."""
        from model_optimizer import recommend_model, get_optimizer_path
        
        with patch('model_optimizer.get_optimizer_path', return_value=tmp_path / "test-opt.json"):
            result = recommend_model("simple formatting task")
            assert "recommendedModel" in result
            assert "tier" in result


class TestSelfImprover:
    """Tests for Self-Improver component."""
    
    def test_load_improvements_creates_default(self, tmp_path):
        """Test that loading non-existent improvements creates default."""
        from self_improver import load_improvements, get_improvement_path
        
        with patch('self_improver.get_improvement_path', return_value=tmp_path / "test-impr.json"):
            data = load_improvements()
            assert data["plans"] == []
            assert data["insights"] == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
